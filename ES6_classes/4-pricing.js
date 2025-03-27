import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a Currency');
    }

    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(Amount) {
    if (typeof Amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = Amount;
  }

  get currency() {
    return this._currency;
  }

  set currency(Currency) {
    if (!(Currency instanceof Currency)) {
      throw new TypeError('Currency must be a Currency');
    }
    this._currency = Currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }
}
