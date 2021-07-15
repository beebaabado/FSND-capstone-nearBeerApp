import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TabsPage } from './tabs.page';

const routes: Routes = [
  {
    path: 'tabs',
    component: TabsPage,
    children: [
      {
        path: 'home',
        loadChildren: () => import('../pages/home/home.module').then(m => m.HomePageModule)
      },
      {
        path: 'beer',
        loadChildren: () => import('../pages/beer/beer.module').then(m => m.BeerPageModule)
      },
      {
        path: 'map',
        loadChildren: () => import('../pages/map/map.module').then(m => m.MapPageModule)
      },
      // {
      //   path: 'test',
      //   loadChildren: () => import('../pages/test/test.module').then(m => m.TestPageModule)
      // },
      {
        path: 'settings',
        loadChildren: () => import('../pages/settings/settings.module').then(m => m.SettingsPageModule)
      },
     // {
     //   path: 'filter-options',
     //   loadChildren: () => import('../pages/filter-options/filter-options.module').then(m => m.FilterOptionsPageModule)
     // },
      {
        path: 'login',
        loadChildren: () => import('../pages/login/login.module').then(m => m.LoginPageModule)
      }
     // {
     //   path: '',
     //   redirectTo: '/tabs/beer',
     //   pathMatch: 'full'
     // }
    ]
  },
  {
    path: '',
    redirectTo: '/tabs/beer',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
})
export class TabsPageRoutingModule {}
