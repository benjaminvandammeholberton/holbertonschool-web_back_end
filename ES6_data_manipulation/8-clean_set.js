function cleanSet(set, startString) {
  const mylist = [];

  set.forEach((item) => {
    if (item.startsWith(startString)) {
      const modifiedItem = item.replace(startString, '');
      mylist.push(modifiedItem);
    }
  });

  return mylist.join('-');
}
module.exports = cleanSet;
