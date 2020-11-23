package com.demo.cache;

import com.demo.doublylist.DoubleLinkedList;
import com.demo.doublylist.DoubleLinkedList.Node;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

/**
 * compare with the LRU, LRU used one doubly linkedlist to implement the algorithm
 * while LFU used a hashmap with key is the frequency and value is a doubly linkedlist of LFUNode
 * @param <K>
 * @param <V>
 */
public class LFUCache<K, V> {
    private int capacity;
    private int size;
    private Map<Integer, DoubleLinkedList> freqMap;
    private Map<K, LFUNode> map;


    public LFUCache(int capacity){
        this.capacity = capacity;
        this.size = 0;
        this.freqMap = new HashMap<>();
        this.map = new HashMap<>();
    }

    private void updateFreq(LFUNode node){
        int freq = node.freq;
        node = (LFUNode) this.freqMap.get(freq).remove(node);

        // delete
        if (this.freqMap.get(freq).getSize() == 0){
            this.freqMap.remove(freq);
        }

        // update
        freq += 1;
        node.freq = freq;
        if (this.freqMap.containsKey(freq) == false){
            this.freqMap.put(freq, new DoubleLinkedList(0xffff));
        }
        this.freqMap.get(freq).append(node);

    }

    public V get(K key){
        if (this.map.containsKey(key) == false){
            return null;
        }

        LFUNode node = this.map.get(key);
        this.updateFreq(node);
        return node.value;
    }

    public void put(K key, V value){
        if (this.capacity == 0){
            return;
        }

        // hit the cache
        if (this.map.containsKey(key)){
            LFUNode node = this.map.get(key);
            node.value = value;
            this.updateFreq(node);
        }

        // did't hit the cache
        else {
            // if the cache is full, then remove the least frequent node
            if (this.capacity <= this.size){
                int minFreq = Collections.min(this.freqMap.keySet());
                Node lowFreqNode = this.freqMap.get(minFreq).pop();
                this.map.remove(lowFreqNode.key);
                this.size --;
            }

            LFUNode node = new LFUNode(key, value);
            node.freq = 1;
            this.map.put(key, node);

            if (this.freqMap.containsKey(node.freq) == false){
                this.freqMap.put(node.freq, new DoubleLinkedList(0xffff));
            }
            this.freqMap.get(node.freq).append(node);
            this.size ++;
        }
    }

    public void print(){
        System.out.println("*********************");
        for (Map.Entry entry: this.freqMap.entrySet()){

            System.out.print("Freq: " + entry.getKey() + " ");
            this.freqMap.get(entry.getKey()).print();

            System.out.println(" ");
        }
        System.out.println("*********************");
    }

    class LFUNode extends Node<K, V>{
        public int freq;

        public LFUNode(K key, V value) {
            super(key, value);
        }
    }

}
