package com.demo.test;

import com.demo.cache.FIFOCache;

public class FIFOCacheDemo {
    public static void main(String[] args) {
        FIFOCache<Integer, Integer> cache = new FIFOCache<>(2);

        cache.put(1, 1);
        cache.print();

        cache.put(2, 2);
        cache.print();

        System.out.println(cache.get(1));

        cache.put(3, 3);
        cache.print();

        System.out.println(cache.get(2));
        cache.print();

        cache.put(4, 4);
        cache.print();

        System.out.println(cache.get(1));
    }
}
