const calculateNumber = require("./0-calcul.js");
const assert = require("assert");

describe("calculateNumber", function () {
  it("add two positive integers", function () {
    assert.equal(calculateNumber(2, 2), 4);
  });

  it("add two positive floats", function () {
    assert.equal(calculateNumber(2.3, 4.6), 7);
  });

  it("add one positive integer and one negative integer", function () {
    assert.equal(calculateNumber(2, -1), 1);
  });

  it("add one positive integer and one negative float", function () {
    assert.equal(calculateNumber(1, -2.4), -1);
  });

  it("add two negative float", function () {
    assert.equal(calculateNumber(-1.4, -2.4), -3);
  });
});
