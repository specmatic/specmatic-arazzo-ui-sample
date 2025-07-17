<script lang="ts">
  import { login } from "../../auth";

  let email = "";
  let password = "";
  let error = "";

  async function handleLogin(e: SubmitEvent) {
    e.preventDefault();
    const res = await fetch("http://localhost:3001/location", {
      method: "POST",
      headers: { "Content-Type": "application/json", internalToken: "API-TOKEN" },
      body: JSON.stringify({ email, password }),
    });

    if (res.ok) {
      const { clientToken, shippingZone } = await res.json();
      login(clientToken, shippingZone);
    } else {
      error = "Invalid credentials";
    }
  }
</script>

<form class="max-w-sm mx-auto mt-20 p-6 bg-white rounded shadow-md space-y-4" on:submit={handleLogin}>
  <h2 class="text-xl font-bold">Login</h2>
  {#if error}
    <div class="text-red-500">{error}</div>
  {/if}
  <input class="w-full border p-2 rounded" type="email" bind:value={email} placeholder="Email" required />
  <input class="w-full border p-2 rounded" type="password" bind:value={password} placeholder="Password" required />
  <button class="w-full bg-blue-500 text-white py-2 rounded cursor-pointer hover:bg-blue-700" type="submit">Login</button>
</form>
