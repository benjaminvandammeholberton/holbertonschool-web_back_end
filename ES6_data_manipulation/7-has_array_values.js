function hasValuesFromArray(mySet, myArray) {
  const allInSet = myArray.every((element) => mySet.has(element));
  if (allInSet) {
    return true;
  } else return false;
}
module.exports = hasValuesFromArray;
