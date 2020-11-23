package com.demo.test;

import com.demo.cache.LFUCache;

public class LFUCacheDemo {
    public static void main(String[] args) {
        LFUCache cache = new LFUCache(2);

        cache.put(1,1);
        cache.print();

        cache.put(2,2);
        cache.print();

        cache.get(1);
        cache.print();

        cache.put(3,3);
        cache.print();

        System.out.println(cache.get(2));
        cache.print();

        System.out.println(cache.get(3));
        cache.print();

        cache.put(4,4);
        cache.print();

        System.out.println(cache.get(1));
        cache.print();

        System.out.println(cache.get(2));
        cache.print();

        System.out.println(cache.get(3));
        cache.print();

        System.out.println(cache.get(4));
        cache.print();

    }
}
