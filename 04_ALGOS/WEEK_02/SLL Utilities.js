class SLLNode {
    constructor(val) {
        this.value = val;
        this.next = null;              
    }
}

class SLL {
    constructor(){
    this.head = null;
    }
    // All Methods built into your class here. Adds a node to the front
    addFront(value){
        var newNode = new SLLNode(value);
        newNode.next = this.head;
        this.head = newNode;
        return this.head // OR you can say return this;
    }
    // Remove a node from the front of the list
    removeFront(){
        if (this.head ==null){
            return this.head;
        }
        var removeNode = this.head; // Have a variable hold the node we'll remove
        this.head = removeNode.next; //Move the head of the list to the 2nd node, which will become the new head when we're down
        removeNode.next = null;
        return this.head;
    }
    // Return the value at the front (head) of the list.
    front(){
        // Edge case: List is empty.
        if (this.head == null){
            return null;
        }
        else { // List is not empty.
            return this.head.value;
        }
    }

/////////////////// SLL Utilities ///////////////////////

    // constructor, other methods, removed for brevity
    contains(value) {
        let runner = this.head;// is "value" to be found anywhere in this list?
        while (runner !== null) {
                if (runner.value == value){
                    return true;
                }
                runner = runner.next;
            }
            return false;
    }

    // constructor, other methods, removed for brevity
    length() {
        let length = 0;
        let runner = this.head;// how many nodes in a list?
        while (runner !== null) {
            length++;
            runner = runner.next;
            }
            return length;
    }

    // constructor, other methods, removed for brevity
    display() {
    let runner = this.head;// neatly display nodes in my list
    while (runner !== null) {
        runner = runner.next;
        console.log(runner.value);
        }
    }
}

var mySLL = new SLL(); //Starts us off with an empty list

mySLL.addFront(10);
mySLL.addFront(5);
mySLL.addFront(3);
mySLL.removeFront();
console.log(mySLL);
// console.log(mySLL.head.next);