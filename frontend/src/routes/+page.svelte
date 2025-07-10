<script lang="ts">
  import { derived } from "svelte/store";
  import "../app.css";
  import { auth } from "../auth.js";
  import Login from "./login/+page.svelte";
  import Products from "./products/+page.svelte";

  const isLoggedIn = derived(auth, ($auth) => $auth.isLoggedIn);
</script>

{#if $isLoggedIn}
  <Products />
{:else}
  <Login />
{/if}
