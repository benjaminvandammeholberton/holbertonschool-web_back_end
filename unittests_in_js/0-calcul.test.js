const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
  it("Checks 1 + 3", function () {
    assert.equal(calculateNumber(1, 3), 4);
  });
});
