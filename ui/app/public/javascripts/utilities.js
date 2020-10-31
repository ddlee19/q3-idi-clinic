function formatNumber(num) {
    console.log("hey")
    let re = new RegExp('/(\d)(?=(\d{3})+(?!\d))/g', '$1,')
    return num.toString().replace(re)
}