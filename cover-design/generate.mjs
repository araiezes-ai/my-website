import * as d3 from 'd3-geo';
import * as d3p from 'd3-geo-projection';
import * as topo from 'topojson-client';
import fs from 'fs';
const world = JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-50m.json'));
const land = topo.merge(world, world.objects.countries.geometries.filter(g=>g.id!=='010'));
const borders = topo.mesh(world, world.objects.countries, (a,b)=>a!==b);
const W=1055,H=1490;
const variant = process.argv[2]||'A';

// hub points (lon,lat): resource regions + Tokyo
const pts = {tokyo:[139.7,35.7], pilbara:[118,-22], qld:[148,-22], chile:[-70,-23], peru:[-71,-15], brazil:[-44,-19], canada:[-120,55], usa:[-110,40], safrica:[27,-26], drc:[26,-11], indonesia:[117,-1], mongolia:[105,46]};

function sphere(cx,cy,r,proj,id='clip'){
  const path=d3.geoPath(proj);
  const grat=d3.geoGraticule().step([20,20])();
  const lines=Object.entries(pts).filter(([k])=>k!=='tokyo').map(([k,p])=>({type:'LineString',coordinates:[pts.tokyo,p]}));
  const dots=Object.entries(pts).map(([k,p])=>{const rot=proj.rotate(), c=[-rot[0],-rot[1]], vis=proj.clipAngle()?d3.geoDistance(p,c)<proj.clipAngle()*Math.PI/180:true; const q=vis&&proj(p);return q?`<circle cx="${q[0].toFixed(1)}" cy="${q[1].toFixed(1)}" r="${k==='tokyo'?6:4}" fill="url(#dot)"/>${k==='tokyo'?`<circle cx="${q[0]}" cy="${q[1]}" r="14" fill="none" stroke="#e8c27a" stroke-width="1" opacity=".8"/>`:''}`:''}).join('');
  return `
  <g>
    <circle cx="${cx}" cy="${cy}" r="${r+18}" fill="url(#halo)"/>
    <circle cx="${cx}" cy="${cy}" r="${r}" fill="url(#ocean)"/>
    <clipPath id="${id}"><circle cx="${cx}" cy="${cy}" r="${r}"/></clipPath><g clip-path="url(#${id})">
      <path d="${path(grat)}" fill="none" stroke="#ffffff" stroke-opacity=".35" stroke-width=".6"/>
      <path d="${path(land)}" fill="url(#land)" filter="url(#landshadow)"/>
      <path d="${path(land)}" fill="url(#mesh)" opacity=".55"/>
      <path d="${path(land)}" fill="url(#warm)" />
      <path d="${path(borders)}" fill="none" stroke="#f3d79a" stroke-opacity=".45" stroke-width=".5"/>
      <path d="${path(land)}" fill="none" stroke="#ffffff" stroke-opacity=".55" stroke-width=".6"/>
      ${lines.map(l=>`<path d="${path(l)}" fill="none" stroke="#e9c27b" stroke-width="1.1" stroke-opacity=".85"/>`).join('')}
      ${dots}
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="url(#shade)"/>
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="url(#gloss)"/>
    </g>
    <circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#ffffff" stroke-opacity=".7" stroke-width="1.5"/>
  </g>`;
}

let cx,cy,r,proj,clip;
if(variant==='A'){
  // polar azimuthal equidistant: every continent on one disc (globe silhouette kept)
  cx=700; cy=880; r=440;
  proj=d3.geoAzimuthalEquidistant().rotate([50,-90,0]).clipAngle(152).scale(r/(150*Math.PI/180)).translate([cx,cy]);
} else {
  // B: two hemispheres — East (Japan/Asia/Australia/Africa) large, West (Americas) smaller
  cx=730; cy=860; r=400;
  proj=d3.geoOrthographic().rotate([-88,-8,0]).scale(r).translate([cx,cy]);
}
let extra='';
if(variant==='B'){
  const c2=[285,1120], r2=200;
  const p2=d3.geoOrthographic().rotate([80,-6,0]).scale(r2).translate(c2);
  extra=sphere(c2[0],c2[1],r2,p2,'clip2');
}
const orbits = `
 <g fill="none" stroke="#c9b48a" stroke-opacity=".55" stroke-width="1">
  <ellipse cx="${cx}" cy="${cy}" rx="${r+250}" ry="${r-40}" transform="rotate(-28 ${cx} ${cy})"/>
  <ellipse cx="${cx+40}" cy="${cy}" rx="${r+120}" ry="${r+140}" transform="rotate(-20 ${cx} ${cy})"/>
  <ellipse cx="${cx}" cy="${cy+30}" rx="${r+330}" ry="${r-180}" transform="rotate(14 ${cx} ${cy})" stroke-opacity=".35"/>
 </g>
 <g fill="#c9a865">
  ${[[cx-r-118,cy-60],[cx-r-60,cy-300],[cx-r+40,cy+300],[cx+r-30,cy-r-40],[cx-r-90,cy+130],[cx+120,cy+r+40]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="3.5"/>`).join('')}
 </g>`;

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
<defs>
 <radialGradient id="ocean" cx="62%" cy="38%" r="70%">
  <stop offset="0" stop-color="#f4f9fd"/><stop offset=".35" stop-color="#cfe2f1"/><stop offset=".75" stop-color="#8fb6d6"/><stop offset="1" stop-color="#5f8fb8"/>
 </radialGradient>
 <radialGradient id="halo" cx="50%" cy="50%" r="50%"><stop offset=".9" stop-color="#9fc3e3" stop-opacity=".35"/><stop offset="1" stop-color="#9fc3e3" stop-opacity="0"/></radialGradient>
 <linearGradient id="land" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4c5d6c"/><stop offset=".5" stop-color="#3a4a59"/><stop offset="1" stop-color="#2f3d4b"/></linearGradient>
 <radialGradient id="warm" gradientUnits="userSpaceOnUse" cx="${variant==='A'?900:820}" cy="${variant==='A'?820:900}" r="420">
  <stop offset="0" stop-color="#f2c983" stop-opacity=".55"/><stop offset=".6" stop-color="#d9a55a" stop-opacity=".18"/><stop offset="1" stop-color="#d9a55a" stop-opacity="0"/></radialGradient>
 <pattern id="mesh" width="22" height="19" patternUnits="userSpaceOnUse">
  <path d="M0 0L11 19L22 0M0 19L22 19M0 0L22 0" fill="none" stroke="#ffffff" stroke-opacity=".22" stroke-width=".5"/>
  <path d="M11 19L0 0L11 0Z" fill="#ffffff" fill-opacity=".05"/>
 </pattern>
 <radialGradient id="shade" cx="65%" cy="35%" r="75%"><stop offset=".55" stop-color="#ffffff" stop-opacity="0"/><stop offset="1" stop-color="#3f6f99" stop-opacity=".35"/></radialGradient>
 <radialGradient id="gloss" cx="74%" cy="30%" r="38%"><stop offset="0" stop-color="#ffffff" stop-opacity=".85"/><stop offset=".5" stop-color="#ffffff" stop-opacity=".25"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>
 <radialGradient id="dot"><stop offset="0" stop-color="#fff6dc"/><stop offset=".5" stop-color="#f0c46e"/><stop offset="1" stop-color="#f0c46e" stop-opacity="0"/></radialGradient>
 <filter id="landshadow"><feDropShadow dx="1" dy="2" stdDeviation="1.5" flood-color="#1d2b38" flood-opacity=".35"/></filter>
 <clipPath id="clip"><circle cx="${cx}" cy="${cy}" r="${r}"/></clipPath>
</defs>
<rect width="${W}" height="${H}" fill="#fbfbfb"/>
${orbits}
${extra}
${sphere(cx,cy,r,proj)}
<g font-family="'Avenir Next','Helvetica Neue',Arial,sans-serif" font-weight="300" fill="#4a4a4a" font-size="34" letter-spacing="1">
 <text x="79" y="207">Mitsubishi Corporation</text>
 <text x="79" y="251">Mineral Resources Group</text>
 <text x="79" y="294">Corporate Profile</text>
</g>
<rect x="79" y="327" width="122" height="2" fill="#e43c3c"/>
<g transform="translate(390,1352)">
 <g fill="#e60012"><path d="M15 0L20 9L15 18L10 9Z"/><path d="M15 18L5 18L0 27L10 27Z"/><path d="M15 18L25 18L30 27L20 27Z"/></g>
 <text x="40" y="27" font-family="Georgia,'Times New Roman',serif" font-size="26" fill="#222">Mitsubishi Corporation</text>
</g>
</svg>`;
fs.writeFileSync(`cover_${variant}.svg`, svg);
