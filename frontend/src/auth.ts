import { writable } from 'svelte/store';
import { browser } from '$app/environment';

const initial = browser ? {
    clientToken: localStorage.getItem('clientToken') || '',
    shippingZone: localStorage.getItem('shippingZone') || '',
    isLoggedIn: !!localStorage.getItem('clientToken')
} : {
    clientToken: '',
    shippingZone: '',
    isLoggedIn: false
};

export const auth = writable(initial);

export function login(clientToken: string, shippingZone: string) {
    localStorage.setItem('clientToken', clientToken);
    localStorage.setItem('shippingZone', shippingZone);
    auth.set({ clientToken, shippingZone, isLoggedIn: true });
}

export function logout() {
    localStorage.removeItem('clientToken');
    localStorage.removeItem('shippingZone');
    auth.set({ clientToken: '', shippingZone: '', isLoggedIn: false });
}
