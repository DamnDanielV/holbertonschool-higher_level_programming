#!/usr/bin/node
const array = process.argv.sort((a, b) => {
    return a - b
})
const verify = (array) => {
    if (array.length < 4 ) {
        console.log(0)
    } else {
        console.log(parseInt(array[3]))
    }
}
verify(array);
