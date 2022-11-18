import Head from 'next/head'
import style from '../styles/Layout.module.css'
import Header from '../components/Header'
import Footer from '../components/Footer'

export default function Layout({title, description,keywords, children}) {
  return (
    <div>
        <Head>
            <title>{title}</title>
            <meta name='description' content={description} />
            <meta name='keywords'    content={keywords}    />
        </Head>
        <Header />
        <div className={style.container}>
          {children}
        </div>
        <Footer />
    </div>
  )
}

Layout.defaultProps = {
    title: 'monEvent',
    description: 'Découvrez de super évènements et activités en résidence',
    keywords: 'évènements, events, activités, résidence, jeux, soirée, laval',
}