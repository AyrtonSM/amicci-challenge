"use client"

import styles from "./page.module.css";
import FormComponent from './components/main-form';
export default function Home() {

  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <FormComponent /> 
      </div>
    </main>
  );
}