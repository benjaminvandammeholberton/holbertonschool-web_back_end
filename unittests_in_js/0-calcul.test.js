const calculateNumber = require("./0-calcul.js");
const assert = require("assert");

describe("Test for calculateNumber", function () {
  it("add two integer numbers", function () {
    assert.equal(calculateNumber(2, 2), 4);
  });

  it("add two float numbers", function () {
    assert.equal(calculateNumber(2.3, 4.6), 7);
  });
});
