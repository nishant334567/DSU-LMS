import "./globals.css";

export const metadata = {
  title: "LENA | Student dashboard",
  description: "Your learning dashboard",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
