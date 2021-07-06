// define
const titleEl = document.querySelector("h1")
const inputEl = document.querySelector("input")
const ulEl    = document.getElementById("arrays")
const arrayEl = document.getElementById("current array")

// main
function main() {
    status("In main.js: running main()")
    // (main() is called on user input -- see handle input at bottom)
    var array = toArray(inputEl)
    advancedSort(array)
}

// sorting algorithm
function advancedSort(array) {
    status("Running sorting algorithm.")
    array = [5, 12, 22, 1, 6, 21, 8, 7]
    var subsets = parse(array)
    subsets.forEach((array) => sort(array))
}

function parse(array) {

    var previous    = array[0] - 1
    var nth         = []
    var subsets     = []

    array.forEach((current) => {
        nth.push(current)
        if (previous > current) {
            subsets.push(nth)
            nth = []
        }
        previous = current
    });

    // for (var i in subsets)
    //     subsets[i] = sort(subsets[i])
    subsets.forEach((array) => showArray(array))
    showArray("Subsets: ⬇️")
    return subsets
}

function sort(array) {
    var previous = array[0]
    array.forEach((current) => {
        if (current < previous) { // SWAP if current & previous are out of order
            status(`Swapping... ${current} and ${previous}`)
            array[i]        = previous
            array[i - 1]    = current
        }
        previous = current
    })

    showArray("Sorted array: " + array)
    return array
}

function swap(array, a, b) {
    var tmp = a
    array[a] = array[b]
    array[b] = tmp
    return array
}

function merge() {

}

function isNumeric(num) {
    if (typeof num === 'string')
        return !isNaN(num)
    return false
}

function toArray(el) {
    // initialize
    
    // text
    var text = new String()
    text = el.value
    text.trim()
    
    if (isArray(text) == "no open bracket" ||
        isArray(text) == "no close bracket") {
        status(isArray(text))
        return false
    }
    
    // array containing split contents of text
    text = removeBrackets(text)
    var array = text.split(',')

    for (var i in array) {
        var val = array[i]
        val = val.trim()
        val = parseInt(val)
        array[i] = val
    }

    showArray(array)
    showArray("Initial Array: ⬇️")
    return array
}

function isArray(arraytext) {
    var initval = arraytext
    var finalval = removeOpenBracket(arraytext)
    if (initval === finalval) return "no open bracket"
    var finalval = removeCloseBracket(arraytext)
    if (initval === finalval) return "no close bracket"
    console.log(`Brackets removed. (from ${arraytext})`)
    return true
}

function removeBrackets(arraytext) {
    console.log(`Removing brackets from ${arraytext}...`)
    arraytext = removeOpenBracket(arraytext)
    arraytext = removeCloseBracket(arraytext)
    return arraytext
}

function removeOpenBracket(arraytext) {
    return arraytext.replace('[', '')
}

function removeCloseBracket(arraytext) {
    return arraytext.replace(']', '')
}

// display
const statEl = document.getElementById("status")
function status(text) {
    prepend(statEl, text)
    console.log(text)
}

function showArray(array) {
    prepend(ulEl, array)
    console.log(`Showing: ${array}`)
    i++
}

function prepend(el, text) {
    el.prepend(document.createElement("br"))
    el.prepend(document.createElement("br"))
    el.prepend(document.createElement("br"))

    el.prepend(
        document.createElement("li").appendChild(
            document.createTextNode(text)))
}

var i = 0

function reset() {
    inputEl.value = ""
    ulEl.innerHTML = ""
    statEl.innerHTML = ""
    arrayEl.innerHTML = ""
}


// handle input
document.addEventListener("keypress", (event) => {
    switch (event.key) {
        case "Enter":
            main()
            break
    }
})

const enterButton = document.getElementById("enter")
enterButton.addEventListener("click", function() {
    main()
})

const resetButton = document.getElementById("reset")
resetButton.addEventListener("click", reset)