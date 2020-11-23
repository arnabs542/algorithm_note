package com.demo.cache;

import com.demo.doublylist.DoubleLinkedList;
import com.demo.doublylist.DoubleLinkedList.Node;

import java.util.HashMap;
import java.util.Map;

public class FIFOCache<K, V> {
    private int capacity;
    private int size;
    private Map<K, Node> map;
    private DoubleLinkedList list;

    public FIFOCache(int capacity){
        this.capacity = capacity;
        this.size = 0;
        this.map = new HashMap<>();
        this.list = new DoubleLinkedList(capacity);
    }

    public V get(K key){
        if (this.map.containsKey(key) == false){
            return null;
        } else {
            Node<K, V> node = this.map.get(key);
            return node.value;
        }
    }

    public void put(K key, V value){
        if (this.capacity == 0){
            return;
        }

        if (map.containsKey(key) == true){
            Node<K, V> node = this.map.get(key);
            this.list.remove(node);
            node.value = value;
            this.list.append(node);
        } else {
            if (this.size == this.capacity){
                Node<K, V> node = this.list.pop();
                this.map.remove(node.key);
                this.size --;
            }

            Node<K, V> node = new Node<>(key, value);
            this.list.append(node);
            this.map.put(key, node);
            this.size ++;
        }
    }

    public void print(){
        this.list.print();
    }
}
