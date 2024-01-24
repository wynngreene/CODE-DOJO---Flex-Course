//1. Multiples of Three – but Not All - DONE!!!
//Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

function one_multi_Three()
{
    for (let i = -300; i < 0; i++)
        {
            if (i != -3 && i != -6 )
        console.log("current number is " + i );
        }
}

one_multi_Three();

//2. Printing Integers with While - DONE!!!
//Print integers from 2000 to 5280, using a WHILE.

function two_integer_Print()
{
    let i = 2000;
    while(i < 5280) {
        console.log("My number is " + i);
        i++;
    }
}

two_integer_Print();

//3. Counting, the Dojo Way
//Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

function three_Count_Five_Ten()
    {
        for (let i = 1; i < 100; i++)
        {
            if (i % 10 == 0){
            console.log("Dojo");
            }
            else if (i % 5 == 0){
            console.log("Coding");
            }
            else
            console.log("Number is " + i);
        };
    }

three_Count_Five_Ten();


//4. Flexible Countdown
//Given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).

function four_Countdown(lowNum, highNum, multNum)
{

}

