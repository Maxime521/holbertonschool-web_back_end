export default class Airport {
    constructor(name, code) {
      this._name = name;
      this._code = code;
    }
  
    get name() {
      return this._name;
    }
  
    get code() {
      return this._code;
    }
  
    get [Symbol.toStringTag]() {
      return this._code;
    }
  
    // Overrides the toString method to return the airport code
    toString() {
      return `[object ${this._code}]`;
    }
  }
