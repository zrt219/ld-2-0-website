import { getQueueStatus } from './campaign-sync.mjs';

getQueueStatus().then(status => {
  console.log('Current Buffer Queue Status:', JSON.stringify(status, null, 2));
}).catch(console.error);
