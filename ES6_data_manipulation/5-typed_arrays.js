/* eslint-disable */
export default function createInt8TypedArray(length, position, value) {
    const buffer = new ArrayBuffer(length);
    const int8 = new Int8Array(buffer);
  
    if (position >= length) {
      throw new Error('Position outside range');
    }
  
    int8[position] = value;
    return new DataView(buffer);
  }
