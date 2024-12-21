// Fungsi Iteratif untuk Mengurutkan Harga
function sortPricesIterative(arr) {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Tukar elemen jika elemen kiri lebih besar dari kanan
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}

// Fungsi Rekursif untuk Mengurutkan Harga
function sortPricesRecursive(arr) {
    if (arr.length <= 1) return arr;

    const pivot = arr[0];
    const left = [];
    const right = [];

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < pivot) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }

    return [...sortPricesRecursive(left), pivot, ...sortPricesRecursive(right)];
}

// Fungsi untuk memproses input (Iteratif)
function processIterative() {
    const input = document.getElementById("inputPrices").value;
    const arr = input.split(",").map(Number);

    const result = sortPricesIterative(arr);

    displayResults(result, "Iteratif");
}

// Fungsi untuk memproses input (Rekursif)
function processRecursive() {
    const input = document.getElementById("inputPrices").value;
    const arr = input.split(",").map(Number);

    const result = sortPricesRecursive(arr);

    displayResults(result, "Rekursif");
}

// Fungsi Menampilkan Hasil
function displayResults(result, method) {
    document.getElementById("sortedResults").innerText = 
        `Hasil Pengurutan (${method}): ${result.join(", ")}`;
}

