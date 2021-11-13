function Ver-StatusPerfil{ 
	param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil)
	Write-Host "Perfil:" $perfil 
	$status = Get-NetFirewallProfile -Name $perfil  
	if($status.enabled){ 
		Write-Host "Status: Activado" 
	} else{ 
		Write-Host "Status: Desactivado" 
	} 
} 


function Cambiar-StatusPerfil{ 
	param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil) 
	$status = Get-NetFirewallProfile -Name $perfil 
	Write-Host "Perfil:" $perfil 
	if($status.enabled){ 
		Write-Host "Status actual: Activado" 
		$opc = Read-Host -Promt "Deseas desactivarlo? [Y] Si [N] No" 
		if ($opc -eq "Y"){ 
			Set-NetFirewallProfile -Name $perfil -Enabled False 
		} 
	} else{ 
		Write-Host "Status: Desactivado" 
		$opc = Read-Host -Promt "Deseas activarlo? [Y] Si [N] No" 
		if ($opc -eq "Y"){ 
			Write-Host "Activando perfil" 
			Set-NetFirewallProfile -Name $perfil -Enabled True 
		} 
	} 
	Ver-StatusPerfil -perfil $perfil 
} 


function Ver-PerfilRedActual{ 
	$perfilRed = Get-NetConnectionProfile 
	Write-Host "Nombre de red:" $perfilRed.Name 
	Write-Host "Perfil de red:" $perfilRed.NetworkCategory 
} 


function Cambiar-PerfilRedActual{ 
	$perfilRed = Get-NetConnectionProfile 
	if($perfilRed.NetworkCategory -eq "Public"){ 
		Write-Host "El perfil actual es público" 
		$opc = Read-Host -Prompt "Quieres cambiar a privado? [Y] Si [N] No" 
		if($opc -eq "Y"){ 
			Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Private 
			Write-Host "Perfil cambiado" 
		} 
	} else{ 
		Write-Host "El perfil actual es privado" 
		$opc = Read-Host -Prompt "Quieres cambiar a público? [Y] Si [N] No" 
		if($opc -eq "Y"){ 
			Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Public
			Write-Host "Perfil cambiado" 
		} 
	} 
	Ver-PerfilRedActual 
} 


function Ver-ReglasBloqueo{ 
	if(Get-NetFirewallRule -Action Block -Enabled True -ErrorAction SilentlyContinue){ 
		Get-NetFirewallRule -Action Block -Enabled True 
	} else{ 
		Write-Host "No hay reglas definidas aún" 
	} 
}


function Agregar-ReglasBloqueo{ 
	$puerto = Read-Host -Prompt "Cuál puerto quieres bloquear?" 
	New-NetFirewallRule -DisplayName "Puerto-Entrada-$puerto" -Profile "Public" -Direction Inbound -Action Block -Protocol TCP -LocalPort $puerto 
}


function Eliminar-ReglasBloqueo{ 
	$reglas = Get-NetFirewallRule -Action Block -Enabled True 
	Write-Host "Reglas actuales" 
	foreach($regla in $reglas){ 
		Write-Host "Regla:" $regla.DisplayName 
		Write-Host "Perfil:" $regla.Profile 
		Write-Host "ID:" $regla.Name 
		$opc = Read-Host -Prompt "Deseas eliminar esta regla [Y] Si [N] No" 
		if($opc -eq "Y"){ 
			Remove-NetFirewallRule -ID $regla.name 
			break 
		} 
	} 
}

do{
    do {
    Write-Host "`n====================== Script========================="
    Write-Host "`ta. Ver Status Perfil"
    Write-Host "`tb. Cambiar Status Perfil"
    Write-Host "`tc. Ver Perfil R ed Actual"
    Write-Host "`td. Cambiar Perfil Red Actual"
    Write-Host "`te. Ver Reglas Bloqueo"
    Write-Host "`tf. Agregar Reglas Bloqueo"
    Write-Host "`tg. Eliminar Reglas Bloqueo"
    Write-Host "`th. Salir'"
    Write-Host "========================================================"
    $choice = Read-Host "`nEnter Choice"
    } until (($choice -eq 'a') -or ($choice -eq 'b') -or ($choice -eq 'c') -or ($choice -eq 'd') -or ($choice -eq 'e') -or ($choice -eq 'f') -or ($choice -eq 'g') -or ($choice -eq 'h'))
    switch ($choice) {
        'a'{
            Ver-StatusPerfil
        }
        'b'{
            Cambiar-StatusPerfil
        }
        'c'{
            Ver-PerfilRedActual
        }
        'd'{
            Cambiar-PerfilRedActual
        }
        'e'{
            Ver-ReglasBloqueo
        }
        'f'{
            Agregar-ReglasBloqueo
        }
        'g'{
            Eliminar-ReglasBloqueo
        }
        'h'{
            Return
        }

    }
}until($choice -eq 'h')