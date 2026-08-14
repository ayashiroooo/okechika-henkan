let mapping = {};
let reverseMapping = {};

fetch("rules.json")
    .then(response => response.json())
    .then(data => {
        mapping = data;

        // 逆変換用の対応表を作る
        reverseMapping = Object.fromEntries(
            Object.entries(mapping).map(([key, value]) => [value, key])
        );
    })
    .catch(error => {
        console.error("rules.jsonの読み込みに失敗しました:", error);
    });


// 順変換
function convertText() {

    const input = document.getElementById("inputText").value;

    const result = [...input].map(function(char) {

        if (mapping[char]) {
            return mapping[char];
        }

        return char;

    }).join("");

    document.getElementById("outputText").value = result;
}


// 逆変換
function reverseConvertText() {

    const input = document.getElementById("inputText").value;

    const result = [...input].map(function(char) {

        return reverseMapping[char] ?? char;

    }).join("");

    document.getElementById("outputText").value = result;
}
