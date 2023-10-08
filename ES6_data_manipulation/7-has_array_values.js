function hasValuesFromArray(mySet, myArray) {
  const allInSet = myArray.every((element) => mySet.has(element));
  if (allInSet) {
    return true;
  }
  return false;
}
module.exports = hasValuesFromArray;
