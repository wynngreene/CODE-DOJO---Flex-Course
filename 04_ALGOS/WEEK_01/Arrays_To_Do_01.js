//Shuffle | DONE!
function array_Shuffle_One(one_Array){
    // thats new!!!
    array.sort(() => Math.random() - 0.5);
    console.log(array);
}
array_Shuffle([17, 62, 28, 94]);

//Fisher–Yates shuffle
function array_Shuffle_Two(Two_Array){
        for(let i = Two_Array - 1; i > 0; i--){
            let random_Num = Math.floor(Math.random() * (i + 1));
            [Two_Array[i]], [Two_Array[random_Num]] = [Two_Array[random_Num]], [Two_Array[i]]
        }
    }
array_Shuffle_Two([17, 62, 28, 94]);


//Skyline Heights
function skyline_View(arr_build_hts){
    let max_build_ht = 0;
    let visible_builds = [];

    for (let i = 0; i < arr_build_hts.length; i++){
        console.log("Max is at " + max_build_ht);
        if (arr_build_hts[i] > max_build_ht){
            //Set to new number.
            max_build_ht = (arr_build_hts[i]);
            console.log("New_Max " + max_build_ht);
            visible_builds.push(arr_build_hts[i]);
            }
        else console.log("Array " + arr_build_hts[i]);
    }
    console.log("New" + visible_builds);
}
let my_Arr = [1,2,9,7,8];
skyline_View(my_Arr);


//Zip It | DONE!
function combine_Array(array_One, array_Two){
    let combo_Array = array_One.concat(array_Two);
    console.log(combo_Array.sort());
}
arr1 = [20, 35, 50]
arr2 = [15, 34, 44]
combine_Array(arr1, arr2)
