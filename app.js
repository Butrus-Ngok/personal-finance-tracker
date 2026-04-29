let expenses = [];

function addExpense() {
    const item = document.getElementById("item").value;
    const amount = parseFloat(document.getElementById("amount").value);

    if (!item || isNaN(amount)) {
        alert("Enter valid data");
        return;
    }

    expenses.push({ item, amount });

    document.getElementById("item").value = "";
    document.getElementById("amount").value = "";

    render();
}

function render() {
    let output = "Item                     Amount ($)\n";
    output += "-----------------------------------\n";

    let total = 0;

    expenses.forEach(e => {
        output += `${e.item.padEnd(25)}${e.amount.toFixed(2)}\n`;
        total += e.amount;
    });

    document.getElementById("output").innerText = output;
}

function saveMonth() {
    const month = document.getElementById("month").value.toUpperCase();
    const income = parseFloat(document.getElementById("income").value);

    if (!month || isNaN(income)) {
        alert("Enter month and income");
        return;
    }

    let total = expenses.reduce((sum, e) => sum + e.amount, 0);
    let savings = income - total;

    let text = `\n===== ${month} =====\n`;
    text += "Item                     Amount ($)\n";
    text += "-----------------------------------\n";

    expenses.forEach(e => {
        text += `${e.item.padEnd(25)}${e.amount.toFixed(2)}\n`;
    });

    text += "-----------------------------------\n";
    text += `Total${" ".repeat(21)}${total.toFixed(2)}\n`;
    text += `Income${" ".repeat(20)}${income.toFixed(2)}\n`;
    text += `Savings${" ".repeat(19)}${savings.toFixed(2)}\n`;
    text += "===================================\n";

    document.getElementById("output").innerText = text;

    // Save to browser storage (like finance.txt)
    localStorage.setItem(month, text);

    expenses = [];
}
