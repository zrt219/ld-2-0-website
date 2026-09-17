import { createBrowserClient } from "@supabase/ssr";

export function createClient() {
  const supabaseUrl =
    process.env.NEXT_PUBLIC_SUPABASE_URL ||
    process.env.SUPABASE_URL ||
    "https://vbfddrqtgdbegtyvmmcp.supabase.co";
  const supabaseAnonKey =
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY ||
    process.env.SUPABASE_ANON_KEY ||
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZiZmRkcnF0Z2RiZWd0eXZtbWNwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk1MTQ5NDUsImV4cCI6MjEwNTA5MDk0NX0.xsyuuo-JSn8rB8bA6uq6uph97tmhZj26TJlre7IBCUg";

  return createBrowserClient(supabaseUrl, supabaseAnonKey);
}
