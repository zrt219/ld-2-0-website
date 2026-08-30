async function checkDeployment() {
  const url = 'https://lornettedaye.com/campaigns/us-open/usopen-01.png';
  console.log(`Checking deployment for ${url}...`);
  for (let attempt = 1; attempt <= 20; attempt++) {
    try {
      const res = await fetch(url, { method: 'HEAD' });
      console.log(`Attempt #${attempt}: Status ${res.status}`);
      if (res.status === 200) {
        console.log('✅ Deployment is LIVE!');
        return true;
      }
    } catch (e) {
      console.log(`Attempt #${attempt} failed: ${e.message}`);
    }
    await new Promise(r => setTimeout(r, 4000));
  }
  return false;
}

checkDeployment().then(isLive => {
  if (!isLive) process.exit(1);
});
