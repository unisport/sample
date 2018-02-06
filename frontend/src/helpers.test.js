import commaSeperate from './helpers/commaSeperate'
import React from 'react';

it('Gives same output', () => {
	expect(commaSeperate(100000)).toBe("1.000,00");
})

it('Gives same output', () => {
	expect(commaSeperate(10)).toBe("0,10");
})

it('Gives same output', () => {
	expect(commaSeperate(123456789)).toBe("1.234.567,89");
})

it('Gives same output', () => {
	expect(commaSeperate("test")).toBe("Prisen findes ikke");
})