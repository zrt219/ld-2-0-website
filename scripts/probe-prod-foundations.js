const https = require('https');

const pages = [
  'https://lornettedaye.com/foundations/select',
  'https://lornettedaye.com/foundations/dashboard',
  'https://lornettedaye.com/foundations/golf',
  'https://lornettedaye.com/foundations/hockey',
  'https://lornettedaye.com/foundations/corporate',
  'https://lornettedaye.com/foundations/europe',
  'https://lornettedaye.com/foundations',
  'https://lornettedaye.com/'
];

function fetchHtml(url) {
  return new Promise((resolve) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ url, status: res.statusCode, html: data }));
    }).on('error', err => resolve({ url, error: err.message }));
  });
}

function probeUrl(fullUrl) {
  return new Promise((resolve) => {
    https.get(fullUrl, (res) => {
      resolve(res.statusCode);
    }).on('error', () => resolve(500));
  });
}

async function audit() {
  const missingUrls = new Set();
  for (const page of pages) {
    const res = await fetchHtml(page);
    if (!res.html) continue;
    const matches = res.html.match(/\/foundations\/[a-zA-Z0-9_\-\.\/]+?\.(?:png|jpg|jpeg|webp|svg)/g) || [];
    for (const m of matches) {
      missingUrls.add(m);
    }
  }

  console.log('Total unique foundations images extracted from production HTML:', missingUrls.size);

  const checkResults = [];
  for (const p of missingUrls) {
    const fullUrl = 'https://lornettedaye.com' + p;
    const status = await probeUrl(fullUrl);
    if (status !== 200) {
      checkResults.push({ path: p, status });
    }
  }
  console.log('Total non-200 on production:', checkResults.length);
  console.log(checkResults);
}
audit();
