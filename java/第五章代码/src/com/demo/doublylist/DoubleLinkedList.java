package com.demo.doublylist;

import java.util.Objects;

public class DoubleLinkedList {
    private int capacity = 0xffff;
    private Node head;
    private Node tail;
    private int size;

    public DoubleLinkedList(int capacity){
        this.capacity = capacity;
        this.size = 0;
    }

    private Node addHead(Node node){
        if (this.head == null){
            this.head = node;
            this.tail = node;
            this.head.next = null;
            this.head.prev = null;
        } else {
            node.next = this.head;
            this.head.prev = node;
            this.head = node;
            this.head.prev = null;
        }

        this.size ++;
        return node;
    }

    private Node addTail(Node node){
        if (this.tail == null){
            this.tail = node;
            this.head = node;
            this.tail.next = null;
            this.tail.prev = null;
        } else {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
            this.tail.next = null;
        }

        this.size ++;
        return node;
    }

    private Node deleteNode(Node node){
        // if node is null, delete tail
        if (node == null){
            node = this.tail;
        }

        if (node.equals(this.tail)){
            this.deleteTail();
        } else if (node.equals(this.head)){
            this.deleteHead();
        } else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
//            node.next = null;
//            node.prev = null;
            this.size --;
        }

        return node;
    }

    // delete from tail
    private Node deleteTail(){
        if (this.tail == null){
            return null;
        }

        Node node = this.tail;
        if (node.prev != null){
            this.tail = node.prev;
            this.tail.next = null;
        } else {
            this.tail = null;
            this.head = null;
        }

        this.size --;
        return node;
    }

    // delete from head
    private Node deleteHead(){
        if (this.head == null){
            return null;
        }

        Node node = this.head;
        if (node.next != null){
            this.head = node.next;
            this.head.prev = null;
        } else {
            this.tail = null;
            this.head = null;
        }

        this.size --;
        return node;
    }

    /**
     * pop the node on the head of the doubly linkedlist
     * @return
     */
    public Node pop(){
        return this.deleteHead();
    }

    /**
     * add the new node at the tail of the doubly linkedlist
     * @param node
     * @return
     */
    public Node append(Node node){
        return this.addTail(node);
    }

    /**
     * add the new node at the head of the double linkedlist
     * @param node
     * @return
     */
    public Node appendFront(Node node){
        return this.addHead(node);
    }

    /**
     * delete the node in the doubly linkedlist
     * @param node
     * @return
     */
    public Node remove(Node node){
        return this.deleteNode(node);
    }

    public void print(){
        Node p = this.head;
        String[] line = new String[this.size];
        int index = 0;

        while (p != null){
            String curr = p.toString();
            p = p.next;

            if (p != null){
                curr = curr + " => ";
            }

            line[index++] = curr;
        }

        for (String l: line){
            System.out.print(l);
        }
        System.out.println("");
    }

    public int getSize(){
        return this.size;
    }

    public static class Node<K, V> {

        public K key;
        public V value;
        public Node prev;
        public Node next;

        public Node(K key, V value){
            this.key = key;
            this.value = value;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "key=" + key +
                    ", value=" + value +
                    '}';
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Node<?, ?> node = (Node<?, ?>) o;
            return Objects.equals(key, node.key) &&
                    Objects.equals(value, node.value);
        }

        @Override
        public int hashCode() {
            return Objects.hash(key, value);
        }
    }

}

