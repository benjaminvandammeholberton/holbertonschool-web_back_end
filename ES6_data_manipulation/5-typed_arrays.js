function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  if (value < -128 || value > 127) {
    throw new Error('Value outside range');
  }
  const buffer = new ArrayBuffer(length);
  const int8View = new Int8Array(buffer);
  int8View[position] = value;
  return buffer;
}
module.exports = createInt8TypedArray;
