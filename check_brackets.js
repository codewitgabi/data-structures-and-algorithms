function checkBracket(brackets) {
  const bracketsDb = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  let stack = [];

  for (let bracket of brackets) {
    if (bracket in bracketsDb) {
      stack.push(bracket);
    } else {
      const lastBracket = stack.pop();

      if (bracket === bracketsDb[lastBracket]) {
        continue;
      } else {
        break;
      }
    }
  }

  return stack.length === 0 ? "Is balanced" : "Not balanced";
}

console.log(checkBracket("{}[()]"));
