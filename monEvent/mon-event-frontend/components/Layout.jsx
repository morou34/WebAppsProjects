import Head from 'next/head'

export default function Layout({title, description,keywords, children}) {
  return (
    <div>
        <Head>
            <title>{title}</title>
            <meta name='description' content={description} />
            <meta name='keywords'    content={keywords}    />
        </Head>
        {children }
    </div>
  )
}

Layout.defaultProps = {
    title: 'monEvent',
    description: 'Découvrez de super évènements et activités en résidence',
    keywords: 'évènements, events, activités, résidence, jeux, soirée, laval',
}