import { ReactNode } from 'react'
import Header from '../layout/Header'

interface LayoutProps {
  children: ReactNode
}

const Layout = ({ children }: LayoutProps) => {
  return (
    <div className="app">
      <Header />
      <main>{children}</main>
    </div>
  )
}

export default Layout

