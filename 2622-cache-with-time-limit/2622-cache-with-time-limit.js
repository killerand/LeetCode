class TimeLimitedCache {
    constructor() {
        this.cache = {};
    }

    set(key, value, duration) {
        const expirationTime = Date.now() + duration;
        if (this.cache.hasOwnProperty(key) && this.cache[key].expirationTime > Date.now()) {
            // Key already exists and has not expired
            this.cache[key] = { value, expirationTime };
            return true;
        } else {
            // New key or expired key
            this.cache[key] = { value, expirationTime };
            return false;
        }
    }

    get(key) {
        if (this.cache.hasOwnProperty(key) && this.cache[key].expirationTime > Date.now()) {
            // Key exists and has not expired
            return this.cache[key].value;
        } else {
            // Key does not exist or has expired
            return -1;
        }
    }

    count() {
        let count = 0;
        const currentTime = Date.now();
        for (const key in this.cache) {
            if (this.cache[key].expirationTime > currentTime) {
                count++;
            }
        }
        return count;
    }
}