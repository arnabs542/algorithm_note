package com.demo.test;

import com.demo.cache.LRUCache;

public class LRUCacheDemo {
    public static void main(String[] args) {
        LRUCache<Integer, Integer> cache = new LRUCache<>(2);
        cache.put(2,2);
        cache.print();

        cache.put(1,1);
        cache.print();

        cache.put(3,3);
        cache.print();

        System.out.println(cache.get(1));
        cache.print();

        System.out.println(cache.get(2));
        cache.print();

        System.out.println(cache.get(3));
        cache.print();
    }
}
