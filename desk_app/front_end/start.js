let entry = document.getElementById("selector");
let no_SPB = document.getElementById("no_SPB");
let Ratio = document.getElementById("Ratio");
let no_students = document.getElementById("no_students");


stu = []
entry.addEventListener("click", function () {
    if (no_students.value != '') {
        stu.push(no_students.value)
        console.log(stu, no_SPB.value, Ratio.value)
        no_students.value = '';
    }
})

let entry1 = document.getElementById("selector1");
let days_name = document.getElementById("days_name");

day = []
entry1.addEventListener("click", function () {
    if (days_name.value != '') {
        day.push(days_name.value)
        days_name.value = '';
    }
    if (days_name.value === "") {
        console.log(days_name.value)
    }
})

function generate() {
    if (no_SPB.value === '' && Ratio.value === '') {
        alert("please enter values of Students per block and Ratio")
    }
    else if (day === []) {
        day = 0
        console.log("days = 0")
        eel.no_stu(stu, no_SPB.value, Ratio.value, day)
    }
    else {
        eel.no_stu(stu, no_SPB.value, Ratio.value, day)
        stu = []
        no_SPB.value = ''
        Ratio.value = ''
        day = []
    }

}

function test() {
    console.log('click')
    eel.tester()
}


