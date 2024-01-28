class BTNode {
    constructor(value) {
        this.val = value;
        this.left = null;
        this.right = null;
    }
}
class BST {
    constructor() {
        this.root = null;
    }
    // add methods here...
    add(val){
        var newNode = new BTNode(val);
        newNode.next = this.root;
        this.root = newNode;
        return this.root;

    }
    contains(val){
        let runner = this.root;
        while (runner){
            if (runner.val == val){
                return true;
            }
            runner = runner.next;
        }
        return false;
    }

    min(){

    }
    
    max(){
        
    }
}

