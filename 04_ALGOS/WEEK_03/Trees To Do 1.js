class BTNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
class BST {
    constructor() {
        this.root = null;
    }
    // add node to binary tree
    add(value){
        this.root = this.addNode(this.root,value);
    }

    //nested functions
    addNode(runner, value) {
        if (runner === null ){
            return new BTNode(value);
        }
        if (value < runner.data){
            runner.left = this.addNode(runner.left, value);
        }
        else if (value > runner.data){
            runner.right = this.addNode(runner.right, value);
        }
        return runner;
    }

    // check if tree contains a specific value
    contains(value){
        return this.containsNode(this.root, value);
    }
    
    //nested functions
    containsNode(runner, value){
        if (runner == null){
            return false;
        }

        if (value === runner.value) {
            return true; 
        }
        else if (value < runner.value){
            return this.containsNode(runner.left, value);
        }
        else {
            return this.containsNode(runner.right, value);
        }
    }

    //Return smallest value 
    min(){
        let runner = this.root;
        let min_Value = this.root.value;

        while (runner.left) {
            if (runner.left.value < min_Value) {
                min_Value = runner.left.value;
            }
            runner = runner.left;
        }
        return min_Value;
    }

    //Return largest value 
    max(){
        let runner = this.root;
        let max_Value = this.root.value;

        while (runner.right) {
            if (runner.right.value < max_Value) {
                max_Value = runner.right.value;
            }
            runner = runner.right;
        }
        return max_Value;        
    }
}

