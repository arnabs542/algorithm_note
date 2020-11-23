package com.demo.cache;

import com.demo.doublylist.DoubleLinkedList;
import com.demo.doublylist.DoubleLinkedList.Node;

import java.util.HashMap;
import java.util.Map;

public class LRUCache<K, V> {
    private int capacity;
    private int size;
    private DoubleLinkedList list;
    private Map<K, Node> map;

    public LRUCache(int capacity){
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.size = 0;
        this.list = new DoubleLinkedList(this.capacity);
    }

    public V get(K key){
        if (this.map.containsKey(key) == true){
            Node<K, V> node = this.map.get(key);
            this.list.remove(node);
            this.list.appendFront(node);
            return node.value;
        } else {
            return null;
        }
    }

    public void put(K key, V value){
        if (this.map.containsKey(key)){
            Node<K, V> node = this.map.get(key);
            this.list.remove(node);
            node.value = value;
            this.list.appendFront(node);
        } else {
            Node<K, V> node = new Node<>(key, value);
            if (this.size >= this.capacity){
                Node<K, V> oldNode = this.list.remove(null);
                this.map.remove(oldNode.key);
                this.size --;
            }

            this.list.appendFront(node);
            this.map.put(key, node);
            this.size ++;

        }
    }

    public void print(){
        this.list.print();
    }

}
