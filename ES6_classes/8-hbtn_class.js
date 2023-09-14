export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  set size(newSize) {
    if (typeof newSize !== 'number') {
      throw new TypeError('size must be a number');
    }
    this._size = newSize;
  }

  set location(newLocation) {
    if (typeof newLocation !== 'string') {
      throw new TypeError('location must be a number');
    }
    this._location = newLocation;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
