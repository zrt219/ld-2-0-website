export class RateLimiter {
  private requestCounts: Map<string, { count: number; windowStart: number }> = new Map();
  private windowMs: number;
  private maxRequests: number;

  constructor(options: { windowMs: number; maxRequests: number }) {
    this.windowMs = options.windowMs;
    this.maxRequests = options.maxRequests;
  }

  isRateLimited(ip: string): boolean {
    const now = Date.now();
    const record = this.requestCounts.get(ip);

    if (!record) {
      this.requestCounts.set(ip, { count: 1, windowStart: now });
      return false;
    }

    if (now - record.windowStart > this.windowMs) {
      // Reset window
      this.requestCounts.set(ip, { count: 1, windowStart: now });
      return false;
    }

    record.count++;
    if (record.count > this.maxRequests) {
      return true;
    }

    return false;
  }
}

export const authRateLimit = new RateLimiter({ windowMs: 60 * 1000, maxRequests: 5 }); // 5 requests per minute
export const apiRateLimit = new RateLimiter({ windowMs: 15 * 60 * 1000, maxRequests: 50 }); // 50 requests per 15 minutes
