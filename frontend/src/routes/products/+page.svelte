<script lang="ts">
  import { onMount } from "svelte";
  import { get } from "svelte/store";
  import { auth, logout } from "../../auth.js";

  let products: Product[] = [];
  let loading: boolean = true;

  onMount(async () => {
    const { clientToken, shippingZone } = get(auth);
    const res = await fetch(`http://localhost:3000/products?shippingZone=${shippingZone}`, {
      headers: { clientToken: clientToken },
    });
    products = await res.json();
    loading = false;
  });

  async function orderProduct(product: Product) {
    const { clientToken } = get(auth);
    const res = await fetch("http://localhost:3000/orders", {
      method: "POST",
      headers: { clientToken: clientToken, "Content-Type": "application/json" },
      body: JSON.stringify({ productId: product.productId, quantity: product.quantity }),
    });

    if (res.ok) {
      const { orderId } = await res.json();
      alert(`Order placed! Order ID: ${orderId}`);
    }
  }
</script>

<div class="h-screen p-10">
  <button class="text-white mb-4 px-4 py-2 bg-blue-500 border rounded fixed right-2 top-2 hover:bg-blue-700 duration-250 cursor-pointer" on:click={logout}>Logout</button>
  {#if loading}
    <div>Loading...</div>
  {:else}
    <table class="w-1/2 m-auto border">
      <thead>
        <tr class="bg-gray-100 *:p-2 *:border">
          <th>ID</th>
          <th>Name</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Order</th>
        </tr>
      </thead>
      <tbody>
        {#each products as product}
          <tr class="*:border text-center *:p-2">
            <td>{product.productId}</td>
            <td>{product.name}</td>
            <td>{product.price}</td>
            <td>{product.quantity}</td>
            <td>
              <button class="bg-green-500 text-white px-2 py-1 rounded cursor-pointer hover:bg-green-600" on:click={() => orderProduct(product)}>Order</button>
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  {/if}
</div>
