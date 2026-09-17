const baseUrl = process.env.BASE_URL || 'http://localhost:3000';

const routes = [
  {
    path: '/foundations/golf',
    expectedImages: [
      'lornette-golf-putting-green-sunrise.png',
      'sunlight-golf-dew-flag.jpg',
      'lornette-golf-coastal-links-sunrise.jpg',
      'sunlight-golf-fairway-sunrise.jpg',
      'lornette-golf-simulator-studio-tablet.png'
    ]
  },
  {
    path: '/foundations/golf/keynote',
    expectedImages: [
      'lornette-golf-keynote-podium.png',
      'lornette-golf-terrace-skyline-view.png'
    ],
    expectedPosition: '85% 18%'
  },
  {
    path: '/foundations/golf/workshop',
    expectedImages: [
      'lornette-golf-indoor-studio.png',
      'lornette-golf-fairway-composure-sunset.jpg',
      'lornette-golf-indoor-green-notebook.png'
    ],
    expectedPosition: '15% 18%'
  },
  {
    path: '/foundations/golf/program',
    expectedImages: [
      'lornette-golf-tournament-prep.png',
      'lornette-golf-executive-desk.png',
      'lornette-golf-fairway-mountain-sunset.png'
    ],
    expectedPosition: '80% 18%'
  },
  {
    path: '/foundations/golf/club-partnership',
    expectedImages: [
      'lornette-golf-coastal-links.png',
      'lornette-golf-clubhouse-lounge-putter.png'
    ],
    expectedPosition: '88% 20%'
  },
  {
    path: '/foundations/clubs',
    expectedImages: [
      'lornette-foundations-executive-desk-runner.png',
      'lornette-foundations-tactical-playbook-board.png'
    ]
  },
  {
    path: '/foundations/performance-edge',
    expectedImages: [
      'lornette-foundations-armchair-study.png',
      'lornette-foundations-curved-track-athletes.png'
    ]
  }
];

async function run() {
  // Test connectivity first
  try {
    const probe = await fetch(baseUrl, { method: 'HEAD' });
  } catch (err) {
    console.error(`\n[ERROR] Unable to reach ${baseUrl}: ${err.message}`);
    console.error('Please make sure Next.js server is running (e.g. `npm run dev` or `npm run start`) or pass BASE_URL=<url>\n');
    process.exit(1);
  }

  let allPass = true;
  for (const r of routes) {
    const url = baseUrl + r.path;
    const res = await fetch(url);
    if (res.status !== 200) {
      console.error(`FAIL: ${r.path} status ${res.status}`);
      allPass = false;
      continue;
    }
    const html = await res.text();
    for (const img of r.expectedImages) {
      if (!html.includes(img)) {
        console.error(`FAIL: ${r.path} missing expected image ${img}`);
        allPass = false;
      } else {
        console.log(`PASS: ${r.path} contains ${img}`);
      }
    }
    if (r.expectedPosition) {
      if (!html.includes(r.expectedPosition)) {
        console.error(`FAIL: ${r.path} missing expected objectPosition ${r.expectedPosition}`);
        allPass = false;
      } else {
        console.log(`PASS: ${r.path} contains objectPosition ${r.expectedPosition}`);
      }
    }
  }
  if (allPass) {
    console.log('\nALL 7 ROUTES PASSED DEEP ASSET AND POSITION AUDIT!');
  } else {
    process.exit(1);
  }
}

run();
