import Image from "next/image";
import styles from "./page.module.css";
import Navbar from "./Components/Navbar";
import Header from "./Components/Header";
import Products from "./Components/Products";
import RelatedProducts from "./Components/RelatedProducts";
import Footer from "./Components/Footer";

export default function Home() {
  return (
   <>
   <Navbar />
   <Header />
   <Products />
   <RelatedProducts />
   <Footer/>
   </>
  );
}
