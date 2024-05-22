<script>
	import '../app.css';

	import { Toaster } from '$lib/components/ui/sonner';

	import Header from './(components)/Header.svelte';
</script>

<Header />
<main class="p-20">
	<slot />
</main>
<Toaster />
